import axios from 'axios';
import { useRouter } from 'next/router';
import { useState } from 'react';

const BASE_URL = process.env.BASE_URL || 'http://localhost:8000';

const CreateFilm = () => {
  const router = useRouter();
  const [title, setTitle] = useState('');
  const [length, setLength] = useState('');
  const [year, setYear] = useState('');
  const [score, setScore] = useState('');
  const [genre, setGenre] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post(`${BASE_URL}/api/films/`, {
        title,
        length: parseInt(length),
        year: parseInt(year),
        score: parseInt(score),
        genre,
      });
      if (response.status === 201) {
        router.push('/');
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Create Film</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>
        <div>
          <label>Length (mins):</label>
          <input type="number" value={length} onChange={(e) => setLength(e.target.value)} />
        </div>
        <div>
          <label>Year:</label>
          <input type="number" value={year} onChange={(e) => setYear(e.target.value)} />
        </div>
        <div>
          <label>Score:</label>
          <input type="number" value={score} onChange={(e) => setScore(e.target.value)} />
        </div>
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default CreateFilm;
