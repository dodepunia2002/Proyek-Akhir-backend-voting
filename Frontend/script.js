const API_URL = "http://127.0.0.1:8000";
let token = localStorage.getItem("access_token");
let candidatesData = []; 

if (token) {
    showSection('dashboard-section');
    loadCandidates();
}

function showSection(id) {
    
    ['login-section', 'register-section', 'dashboard-section'].forEach(sec => {
        document.getElementById(sec).classList.add('hidden');
    });

    // Sembunyikan sub-view di dashboard jika masuk dashboard
    if (id === 'dashboard-section') {
        document.getElementById('dashboard-section').classList.remove('hidden');
        // Default view di dashboard biasanya list, tapi fungsi pemanggil yang atur
    } else {
        document.getElementById(id).classList.remove('hidden');
    }
    
    showMessage(""); 
}

function showMessage(msg, type = 'success') {
    const box = document.getElementById('message-box');
    if (!msg) {
        box.innerHTML = "";
        return;
    }
    box.innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
}

async function handleLogin() {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    const formData = new URLSearchParams();
    formData.append('username', email); 
    formData.append('password', password);

    try {
        const res = await fetch(`${API_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: formData
        });

        if (!res.ok) throw new Error("Login Gagal. Cek email/password.");
        
        const data = await res.json();
        token = data.access_token;
        localStorage.setItem("access_token", token);
        
        showMessage("Login Berhasil!");
        setTimeout(() => {
            showSection('dashboard-section');
            loadCandidates();
        }, 1000);
    } catch (err) {
        showMessage(err.message, 'error');
    }
}

async function handleRegister() {
    const username = document.getElementById('reg-username').value;
    const email = document.getElementById('reg-email').value;
    const password = document.getElementById('reg-password').value;

    try {
        const res = await fetch(`${API_URL}/auth/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        });

        if (!res.ok) {
            const errData = await res.json();
            throw new Error(errData.detail || "Gagal Mendaftar");
        }

        showMessage("Registrasi Berhasil! Silakan Login.");
        setTimeout(() => showSection('login-section'), 1500);
    } catch (err) {
        showMessage(err.message, 'error');
    }
}

function handleLogout() {
    localStorage.removeItem("access_token");
    token = null;
    showSection('login-section');
    showMessage("Anda telah logout.");
}


async function loadCandidates() {

    document.getElementById('vote-view').classList.remove('hidden');
    document.getElementById('results-view').classList.add('hidden');
    document.getElementById('add-candidate-view').classList.add('hidden');
    document.getElementById('edit-candidate-view').classList.add('hidden');

    try {
        const res = await fetch(`${API_URL}/candidates/`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        candidatesData = await res.json();
        
        const list = document.getElementById('candidates-list');
        list.innerHTML = "";

        if (candidatesData.length === 0) {
            list.innerHTML = "<p>Belum ada kandidat.</p>";
            return;
        }

        candidatesData.forEach(cand => {
            list.innerHTML += `
                <div class="candidate-card">
                    <div class="candidate-info">
                        <div class="candidate-name">${cand.name}</div>
                        <small>${cand.description}</small>
                    </div>
                    <div class="candidate-actions">
                        <button onclick="handleVote(${cand.id})">Vote</button>
                        <button class="btn-warning" onclick="showEditForm(${cand.id})">Edit</button>
                        <button class="btn-danger" onclick="handleDeleteCandidate(${cand.id})">Hapus</button>
                    </div>
                </div>
            `;
        });
    } catch (err) {
        console.error(err);
    }
}

function showAddCandidate() {
    document.getElementById('vote-view').classList.add('hidden');
    document.getElementById('results-view').classList.add('hidden');
    document.getElementById('edit-candidate-view').classList.add('hidden');
    document.getElementById('add-candidate-view').classList.remove('hidden');
}

async function handleAddCandidate() {
    const name = document.getElementById('cand-name').value;
    const desc = document.getElementById('cand-desc').value;

    try {
        const res = await fetch(`${API_URL}/candidates/`, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ name: name, description: desc })
        });

        if (!res.ok) throw new Error("Gagal menambah kandidat");

        showMessage("Kandidat berhasil ditambahkan!");
        document.getElementById('cand-name').value = "";
        document.getElementById('cand-desc').value = "";
        loadCandidates(); 
    } catch (err) {
        showMessage(err.message, 'error');
    }
}

function showEditForm(id) {
    const candidate = candidatesData.find(c => c.id === id);
    if (!candidate) return;

    document.getElementById('edit-cand-id').value = candidate.id;
    document.getElementById('edit-cand-name').value = candidate.name;
    document.getElementById('edit-cand-desc').value = candidate.description;

    document.getElementById('vote-view').classList.add('hidden');
    document.getElementById('edit-candidate-view').classList.remove('hidden');
}

async function handleUpdateCandidate() {
    const id = document.getElementById('edit-cand-id').value;
    const name = document.getElementById('edit-cand-name').value;
    const desc = document.getElementById('edit-cand-desc').value;

    try {
        const res = await fetch(`${API_URL}/candidates/${id}`, {
            method: 'PUT',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ name: name, description: desc })
        });

        if (!res.ok) throw new Error("Gagal mengupdate kandidat");

        showMessage("Kandidat berhasil diupdate!");
        loadCandidates();
    } catch (err) {
        showMessage(err.message, 'error');
    }
}

async function handleDeleteCandidate(id) {
    if(!confirm("Yakin ingin menghapus kandidat ini? Data yang dihapus tidak bisa dikembalikan.")) return;

    try {
        const res = await fetch(`${API_URL}/candidates/${id}`, {
            method: 'DELETE',
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (!res.ok) throw new Error("Gagal menghapus kandidat");

        showMessage("Kandidat berhasil dihapus!");
        loadCandidates();
    } catch (err) {
        showMessage(err.message, 'error');
    }
}

async function handleVote(candidateId) {
    if(!confirm("Yakin ingin memilih kandidat ini?")) return;

    try {
        const res = await fetch(`${API_URL}/votes/`, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ candidate_id: candidateId })
        });

        if (!res.ok) {
            const errData = await res.json();
            throw new Error(errData.detail || "Gagal Vote");
        }

        showMessage("Suara berhasil masuk! Terima kasih.");
        loadResults(); 
    } catch (err) {
        showMessage(err.message, 'error');
    }
}

async function loadResults() {
    document.getElementById('vote-view').classList.add('hidden');
    document.getElementById('results-view').classList.remove('hidden');
    document.getElementById('add-candidate-view').classList.add('hidden');
    document.getElementById('edit-candidate-view').classList.add('hidden');

    try {
        const res = await fetch(`${API_URL}/votes/results`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await res.json();

        let html = `<table class="results-table">
            <thead><tr><th>Nama Kandidat</th><th>Jumlah Suara</th></tr></thead>
            <tbody>`;
        
        data.forEach(row => {
            html += `<tr><td>${row.candidate_name}</td><td><strong>${row.total_votes}</strong></td></tr>`;
        });

        html += `</tbody></table>`;
        document.getElementById('results-content').innerHTML = html;
    } catch (err) {
        console.error(err);
    }
}