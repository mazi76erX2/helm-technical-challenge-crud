import axios from 'axios';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

const BASE_URL: string = process.env.NEXT_PUBLIC_BASE_URL || 'http://localhost:8000';

type Film = {
  id: number;
  title: string;
  length: number;
  year: number;
  score: number;
  genre: string;
};

const EditFilm = () => {
  const router = useRouter();
  const { filmId } = router.query;
  const [film, setFilm] = useState<Film | null>(null);
  const [title, setTitle] = useState('');
  const [length, setLength] = useState('');
  const [year, setYear] = useState('');
  const [score, setScore] = useState('');
  const [genre, setGenre] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${BASE_URL}/api/films/${filmId}/`);
        setFilm(response.data);
        setTitle(response.data.title);
        setLength(response.data.length.toString());
        setYear(response.data.year.toString());
        setScore(response.data.score.toString());
        setGenre(response.data.genre);
      } catch (error) {
        setError('Failed to fetch film details.');
        console.error(error);
      }
    };

    if (filmId) {
      fetchData();
    }
  }, [filmId]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.put(`${BASE_URL}/api/films/${filmId}/`, {
        title,
        length: parseInt(length),
        year: parseInt(year),
        score: parseInt(score),
        genre,
      });
      if (response.status === 200) {
        router.push('/');
      }
    } catch (error) {
      setError('Failed to update film.');
      console.error(error);
    }
  };

  if (!film) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {error && <div>{error}</div>}
      <h1>Edit Film</h1>
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
        <div>
          <label>Genre:</label>
          <input type="text" value={genre} onChange={(e) => setGenre(e.target.value)} />
        </div>
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default EditFilm;
