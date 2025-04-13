// /frontend/js/profile.js

document.addEventListener('DOMContentLoaded', function () {
    const token = localStorage.getItem('access_token');

    fetch('http://127.0.0.1:8000/api/profile/', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('username').value = data.username;
        document.getElementById('email').value = data.email;
        document.getElementById('first_name').value = data.first_name;
        document.getElementById('last_name').value = data.last_name;
        document.getElementById('role').value = data.role;
    })
    .catch(error => console.error('Error:', error));
});

// Handle profile update
document.getElementById('profile-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const token = localStorage.getItem('access_token');
    const payload = {
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value
    };

    fetch('http://127.0.0.1:8000/api/profile/update/', {
        method: 'PUT',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        alert('Profile updated successfully!');
    })
    .catch(error => {
        console.error('Error updating profile:', error);
        alert('Failed to update profile.');
    });
});

function goBack() {
    window.location.href = "index.html";
}


