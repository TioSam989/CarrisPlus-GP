const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Serve static files from build directory
app.use(express.static(path.join(__dirname, 'build')));

// Handle React routing - return index.html for all routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Listen on PORT and 0.0.0.0
app.listen(port, '0.0.0.0', () => {
  console.log(`Server is running on port ${port}`);
});
