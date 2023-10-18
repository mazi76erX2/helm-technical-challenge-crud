import axios from 'axios';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

type Film = {
  id: number;
  title: string;
  length: number;
  year: number;
  score: number;
  genre: string;
};

const FilmDetail = () => {
  const router = useRouter();
  const { filmId } = router.query;
  const [film, setFilm] = useState<Film | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`/api/films/${filmId}/`);
        setFilm(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    if (filmId) {
      fetchData();
    }
  }, [filmId]);

  if (!film) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{film.title}</h1>
      <p>Length: {film.length} mins</p>
      <p>Year: {film.year}</p>
      <p>Score: {film.score}</p>
      <p>Genre: {film.genre}</p>
    </div>
  );
};

export default FilmDetail;
