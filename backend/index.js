// backend/index.js
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json()); // To parse JSON bodies

// Basic health check
app.get('/', (req, res) => {
  res.send('PASO API is running!');
});

// Placeholder route for portfolio recommendation
app.post('/recommend', (req, res) => {
  const { risk_level, horizon_years } = req.body;

  if (!risk_level || !horizon_years) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  // For now: just echo the input
  return res.json({
    message: 'Received input',
    risk_level,
    horizon_years,
  });
});

app.listen(PORT, () => {
  console.log(`PASO backend is running on port ${PORT}`);
});
