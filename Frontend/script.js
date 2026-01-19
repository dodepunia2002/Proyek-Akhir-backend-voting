const API_URL = "http://127.0.0.1:8000";
let token = localStorage.getItem("access_token");
let currentPollId = null;

// --- BAGIAN UTAMA ---
if (token) {
    loadPolls();
    loadUserProfile(); 
} else {
    showSection('login-section');
}

function showSection(id) {
    ['login-section', 'register-section', 'polls-section', 'poll-detail-section'].forEach(sec => {
        document.getElementById(sec).classList.add('hidden');
    });
    document.getElementById(id).classList.remove('hidden');
    showMessage(""); 
}

function showMessage(msg, type = 'success') {
    const box = document.getElementById('message-box');
    if (!msg) { box.innerHTML = ""; return; }
    box.innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
}

async function loadUserProfile() {
    try {
        const res = await fetch(`${API_URL}/auth/me`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
            const user = await res.json();
            const display = document.getElementById('user-display');
            if (display) {
                display.innerText = `Halo, ${user.username} (${user.role})!`;
            }
            localStorage.setItem("current_user_id", user.id);
            localStorage.setItem("current_user_role", user.role);
        }
    } catch (err) { console.error("Gagal load profil", err); }
}

// --- AUTH ---
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
        if (!res.ok) throw new Error("Login Gagal");
        const data = await res.json();
        token = data.access_token;
        localStorage.setItem("access_token", token);
        
        loadUserProfile(); 
        loadPolls();
    } catch (err) { showMessage(err.message, 'error'); }
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
            const err = await res.json();
            throw new Error(err.detail || "Gagal Daftar");
        }
        showMessage("Registrasi Berhasil! Silakan Login.");
        showSection('login-section');
    } catch (err) { showMessage(err.message, 'error'); }
}

function handleLogout() {
    localStorage.removeItem("access_token");
    token = null;
    showSection('login-section');
}


async function loadPolls() {
    showSection('polls-section');
    document.getElementById('create-poll-form').classList.add('hidden');
    document.getElementById('edit-poll-form').classList.add('hidden');

    try {
        const res = await fetch(`${API_URL}/polls/`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const polls = await res.json();
        const list = document.getElementById('polls-list');
        list.innerHTML = "";
        
        if (polls.length === 0) { list.innerHTML = "<p>Belum ada polling.</p>"; return; }

        polls.forEach(p => {
            const deadline = new Date(p.deadline).toLocaleString();
          
            list.innerHTML += `
                <div class="candidate-card">
                    <div class="candidate-info">
                        <div class="candidate-name">${p.title}</div>
                        <small>${p.description}</small><br>
                        <small style="color:red">Batas: ${deadline}</small>
                    </div>
                    <div style="display:flex; gap:5px; margin-top:10px;">
                        <button onclick="openPoll(${p.id}, '${p.title}', '${p.description}', '${deadline}')">Buka</button>
                        <button class="btn-warning" onclick="openEditPoll(${p.id}, '${p.title}', '${p.description}', '${p.deadline}')">Edit</button>
                        <button class="btn-danger" onclick="deletePoll(${p.id})">Hapus</button>
                    </div>
                </div>`;
        });
    } catch (err) { console.error(err); }
}

function showCreatePollForm() {
    document.getElementById('edit-poll-form').classList.add('hidden'); // Tutup edit jika ada
    document.getElementById('create-poll-form').classList.remove('hidden');
}


function openEditPoll(id, title, desc, deadlineRaw) {
    document.getElementById('create-poll-form').classList.add('hidden'); // Tutup create jika ada
    document.getElementById('edit-poll-form').classList.remove('hidden');
    
   
    document.getElementById('edit-poll-id').value = id;
    document.getElementById('edit-poll-title').value = title;
    document.getElementById('edit-poll-desc').value = desc;
    
    
    if(deadlineRaw) {
        document.getElementById('edit-poll-deadline').value = deadlineRaw.slice(0, 16);
    }
    
 
    window.scrollTo(0, 0);
}

async function handleUpdatePoll() {
    const id = document.getElementById('edit-poll-id').value;
    const title = document.getElementById('edit-poll-title').value;
    const desc = document.getElementById('edit-poll-desc').value;
    const deadline = document.getElementById('edit-poll-deadline').value;

    try {
        const res = await fetch(`${API_URL}/polls/${id}`, {
            method: 'PUT', 
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
            body: JSON.stringify({ title, description: desc, deadline: deadline })
        });
        
        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || "Gagal Update (Hanya Admin/Pembuat yg bisa)");
        }
        showMessage("Polling berhasil diupdate!");
        document.getElementById('edit-poll-form').classList.add('hidden');
        loadPolls(); // Refresh daftar
    } catch (err) { showMessage(err.message, 'error'); }
}


async function handleCreatePoll() {
    const title = document.getElementById('new-poll-title').value;
    const desc = document.getElementById('new-poll-desc').value;
    const deadline = document.getElementById('new-poll-deadline').value;

    try {
        const res = await fetch(`${API_URL}/polls/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
            body: JSON.stringify({ title, description: desc, deadline: deadline })
        });
        if (!res.ok) throw new Error("Gagal buat polling");
        showMessage("Polling dibuat!");
        document.getElementById('create-poll-form').classList.add('hidden');
        loadPolls();
    } catch (err) { showMessage(err.message, 'error'); }
}

async function deletePoll(id) {
    if(!confirm("Hapus polling ini?")) return;
    try {
        const res = await fetch(`${API_URL}/polls/${id}`, {
            method: 'DELETE', 
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if(!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || "Gagal hapus (Hanya Admin/Pembuat yang bisa)");
        }
        showMessage("Polling dihapus");
        loadPolls();
    } catch (err) { showMessage(err.message, 'error'); }
}

// --- DETAIL POLL & CANDIDATES ---
function openPoll(id, title, desc, deadline) {
    currentPollId = id;
    document.getElementById('poll-title-display').innerText = title;
    document.getElementById('poll-desc-display').innerText = desc;
    document.getElementById('poll-deadline-display').innerText = deadline;
    showSection('poll-detail-section');
    loadCandidates(id);
}

async function loadCandidates(pollId) {
    document.getElementById('results-view').classList.add('hidden');
    document.getElementById('candidates-view').classList.remove('hidden');
    document.getElementById('add-candidate-view').classList.add('hidden');
    
    try {
        const res = await fetch(`${API_URL}/candidates/`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const allCandidates = await res.json();
        const candidates = allCandidates.filter(c => c.poll_id === pollId);

        const list = document.getElementById('candidates-list');
        list.innerHTML = "";
        
        if (candidates.length === 0) { list.innerHTML = "<p>Belum ada kandidat.</p>"; return; }

        candidates.forEach(cand => {
            list.innerHTML += `
                <div class="candidate-card">
                    <div class="candidate-info">
                        <div class="candidate-name">${cand.name}</div>
                        <small>${cand.description}</small>
                    </div>
                    <button onclick="handleVote(${cand.id})">Vote</button>
                </div>`;
        });
    } catch (err) { console.error(err); }
}

function showAddCandidate() {
    document.getElementById('add-candidate-view').classList.remove('hidden');
}

async function handleAddCandidate() {
    const name = document.getElementById('cand-name').value;
    const desc = document.getElementById('cand-desc').value;

    try {
        const res = await fetch(`${API_URL}/candidates/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
            body: JSON.stringify({ name, description: desc, poll_id: currentPollId })
        });
        if (!res.ok) throw new Error("Gagal tambah kandidat");
        showMessage("Kandidat ditambah!");
        document.getElementById('add-candidate-view').classList.add('hidden');
        loadCandidates(currentPollId);
    } catch (err) { showMessage(err.message, 'error'); }
}

async function handleVote(candidateId) {
    if(!confirm("Yakin pilih ini?")) return;
    try {
        const res = await fetch(`${API_URL}/votes/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
            body: JSON.stringify({ poll_id: currentPollId, candidate_id: candidateId })
        });
        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || "Gagal Vote");
        }
        showMessage("Berhasil Vote!");
    } catch (err) { showMessage(err.message, 'error'); }
}

async function loadResults(pollId) {
    document.getElementById('candidates-view').classList.add('hidden');
    document.getElementById('add-candidate-view').classList.add('hidden');
    document.getElementById('results-view').classList.remove('hidden');

    try {
        const res = await fetch(`${API_URL}/votes/results/${pollId}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        
        if (!res.ok) {
            const err = await res.json();
            document.getElementById('results-content').innerHTML = `<p style="color:red; text-align:center;">${err.detail}</p>`;
            return;
        }

        const data = await res.json();
        let html = `<table class="results-table"><thead><tr><th>Kandidat</th><th>Suara</th></tr></thead><tbody>`;
        data.forEach(r => {
            html += `<tr><td>${r.candidate_name}</td><td>${r.total_votes}</td></tr>`;
        });
        html += `</tbody></table>`;
        document.getElementById('results-content').innerHTML = html;
    } catch (err) { console.error(err); }
}