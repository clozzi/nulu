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
        <ol>
          {users.length > 0 ? (
            users.map(user => (
              <li key={user.id}>{user.name}</li>
            ))
          ) : (
            <p>No Users</p>
          )}
        </ol>
      </div>
    </>
  )
}

export default App
