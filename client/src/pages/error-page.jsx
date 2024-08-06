import { useRouteError } from "react-router-dom";

function ErrorPage() {
    const error = useRouteError();
    console.error(error);

    return (
        <div id="error-page">
            <h1>Uh-oh!</h1>
            <p>You broke me!</p>
            <p>{error.statusText || error.message}</p>
        </div>
    );
};

export default ErrorPage;