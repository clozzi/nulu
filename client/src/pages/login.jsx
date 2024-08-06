import { Link } from "react-router-dom";


function Login() {
    return (
        <div>
            <p>Login form will go here</p>
            <button>once clicked, if successful, redirect to /users/:id</button>
            <Link to={'/signup'} >New User? Click here</Link>
        </div>
    );
};

export default Login;