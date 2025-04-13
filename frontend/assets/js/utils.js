const API_BASE_URL = "http://127.0.0.1:8000"; // Change if needed

// Get token from localStorage
function getAuthToken() {
  return localStorage.getItem("access_token");
}

// API Request function
async function apiRequest(endpoint, method = "GET", body = null) {
  const headers = {
    "Content-Type": "application/json",
  };

  const token = getAuthToken();
  if (token) headers["Authorization"] = `Bearer ${token}`;

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : null,
  });

  // Auto-refresh token if expired (optional, we can add later)
  if (response.status === 401) {
    alert("Unauthorized or token expired. Please login again.");
    window.location.href = "/pages/login.html";
  }

  return response.json();
}
 
