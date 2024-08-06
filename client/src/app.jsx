import { useEffect, useState } from "react"

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
    .then(r => r.json())
    .then(data => {
      setUsers(data)
    })
  }, [])

  return (
    <>
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
  )
}

export default App
