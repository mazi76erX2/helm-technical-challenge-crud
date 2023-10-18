import Link from 'next/link';

const Home = () => {
  return (
    <div className="container mx-auto">
      <h1>Film List</h1>
      <ul>
        {/* Film List */}
        <li>
          <Link href="/">View All Films</Link>
        </li>
        {/* Create Film */}
        <li>
          <Link href="/create">Create Film</Link>
        </li>
      </ul>
    </div>
  );
};

export default Home;

