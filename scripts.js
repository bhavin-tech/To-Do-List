let notes = [];
let editIndex = -1;

function addNote() {
    const noteTitle = document.getElementById('noteTitle').value.trim();
    const noteDescription = document.getElementById('noteDescription').value.trim();
    const notesTable = document.getElementById('notesTable').getElementsByTagName('tbody')[0];
    
    if (noteTitle === '' || noteDescription === '') {
        alert('Please enter both title and description.');
        return;
    }

    const dateTime = new Date().toLocaleString();

    if (editIndex === -1) {
        notes.push({ title: noteTitle, description: noteDescription, dateTime });
    } else {
        notes[editIndex] = { title: noteTitle, description: noteDescription, dateTime };
        editIndex = -1;
    }

    renderNotes();
    clearInputs();
}

function renderNotes() {
    const notesTableBody = document.getElementById('notesTable').getElementsByTagName('tbody')[0];
    notesTableBody.innerHTML = '';

    notes.forEach((note, index) => {
        const row = notesTableBody.insertRow();
        const cellSrNo = row.insertCell(0);
        const cellTitle = row.insertCell(1);
        const cellDescription = row.insertCell(2);
        const cellDateTime = row.insertCell(3);
        const cellActions = row.insertCell(4);

        cellSrNo.textContent = index + 1;
        cellTitle.textContent = note.title;
        cellDescription.textContent = note.description;
        cellDateTime.textContent = note.dateTime;
        cellActions.innerHTML = `
            <button class="edit" onclick="editNote(${index})">Edit</button>
            <button class="delete" onclick="deleteNote(${index})">Delete</button>
        `;
    });
}

function clearInputs() {
    document.getElementById('noteTitle').value = '';
    document.getElementById('noteDescription').value = '';
}

function editNote(index) {
    const note = notes[index];
    document.getElementById('noteTitle').value = note.title;
    document.getElementById('noteDescription').value = note.description;
    editIndex = index;
}

function deleteNote(index) {
    notes.splice(index, 1);
    renderNotes();
}