import { createContext, useEffect, useState } from 'react';


const UserContext = createContext({});

function UserProvider({ children }) {
    const [user, setUser] = useState(null);

    useEffect(() => {
        fetch("/api/check_session")
        .then(r => {
            if (r.ok) {
                r.json()
                .then(data => {setUser(data), console.log(data)})
            }
        })
    }, []);

    return <UserContext.Provider value={{ user, setUser }}>{ children }</UserContext.Provider>
}

export { UserContext, UserProvider }