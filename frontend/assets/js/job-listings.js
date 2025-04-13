// /frontend/js/job-listings.js

document.addEventListener('DOMContentLoaded', function () {
    const token = localStorage.getItem('access_token');

    fetch('http://127.0.0.1:8000/api/jobs/', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        const jobsContainer = document.getElementById('jobs-container');
        jobsContainer.innerHTML = '';

        data.forEach(job => {
            const jobElement = document.createElement('div');
            jobElement.className = 'job-card';
            jobElement.innerHTML = `
                <h3>${job.title}</h3>
                <p><strong>Company:</strong> ${job.company_name}</p>
                <p><strong>Description:</strong> ${job.description}</p>
                <p><strong>Location:</strong> ${job.location}</p>
                <p><strong>Salary:</strong> ${job.salary}</p>
                <button onclick="applyJob(${job.id})">Apply</button>
            `;
            jobsContainer.appendChild(jobElement);
        });
    })
    .catch(error => console.error('Error:', error));
});

function applyJob(jobId) {
    const token = localStorage.getItem('access_token');

    fetch(`http://127.0.0.1:8000/api/jobs/${jobId}/apply/`, {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            alert('Applied successfully!');
        } else {
            alert('Failed to apply.');
        }
    })
    .catch(error => console.error('Error:', error));
}

function goBack() {
    window.location.href = "index.html";
}

