import { useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../context/user-context";


function Login() {
    const navigate = useNavigate()
    const { user, setUser } = useContext(UserContext);
    const [name, setName] = useState(null);
    const [password, setPassword] = useState(null);

    function handleLogin(e) {
        e.preventDefault()
        fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ name, password }),
        })
        .then(r => r.json())
        .then(user => {
            console.log(user),
            setUser(user),
            navigate("/home")
        })
    }

    
    return (
        <div>
            <form onSubmit={handleLogin}>
                <label>Enter Name: </label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                <label>Enter Password: </label>
                <input type="text" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Login</button>
            </form>
            <Link to={'/signup'} >New User? Click here</Link>
        </div>
    );
};

export default Login;