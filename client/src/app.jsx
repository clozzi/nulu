import { useEffect, useState } from "react";
import Login from "./pages/login";
import Home from "./pages/home";

function App() {
  const [user, setUser] = useState(null)
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
    .then(r => r.json())
    .then(data => {
      setUsers(data)
      // setUser(data[0])
    })
  }, []);

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
      </div>
    </>
  );
};

export default App;
