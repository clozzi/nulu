import { useEffect, useState } from "react";
import Login from "./pages/login";
import Home from "./pages/home";

function App() {
  const [user, setUser] = useState(null);
  const [users, setUsers] = useState([]);
  const [medias, setMedias] = useState([]);

  useEffect(() => {
    fetch('/api/users')
    .then(r => r.json())
    .then(data => {
      setUsers(data)
    })
  }, []);

  useEffect(() => {
    fetch('/api/medias')
    .then(r => r.json())
    .then(data => {
      setMedias(data)
    })
  }, [])

  return (
    <>
    {user ? (
      <Home />
    ):(
      <Login />
    )}
      <div>
        <p>Hello</p>
        <label>Current Users: </label>
        {users.length > 0 ? (
          <ul>
            {users.map((user) => (
              <li key={user.id}>
                {user.name}
              </li>
            ))}
          </ul>
        ): (
          <p>No Users</p>
        )}
        <label>Current Media: </label>
        {medias.length > 0 ? (
          <ul>
            {medias.map((media) => (
              <li key={media.id}>
                {media.title}
              </li>
            ))}
          </ul>
        ): (
          <p>No Media</p>
        )}
      </div>
    </>
  );
};

export default App;
