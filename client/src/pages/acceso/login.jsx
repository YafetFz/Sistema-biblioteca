import axios from "axios"; // Librería para hacer peticiones HTTP
import "../../styles/acceso/login.css";

export default function Login() {
    const login = async () => {
        try {
            // "http://localhost:3001/login" es la URL del servidor
            // "/login" es la ruta API que se está llamando
            // { email: "texto desde el input", password: "texto desde el input" } es el objeto que se está enviando al servidor
            // response es la respuesta del servidor
            // axios.post() es una función asíncrona que envía una petición POST al servidor
            // await es una palabra clave que indica que la función debe esperar a que la petición termine
            const response = await axios.post("http://127.0.0.1:5000/login", {
                email: "texto desde el input",
                password: "texto desde el input",
            });

            // Enviar la respuesta del servidor a la consola
            console.log(response);
        } catch (error) {
            // Si hubo un error, enviarlo a la consola
            console.error(error);
        }
    };

    return (
        <main>
            <p>Esta es la pag de login</p>
            <br />
            <br />

            <form>
                <label htmlFor="email">Correo electrónico</label>
                <input type="email" id="email" name="email" />
                <br />

                <label htmlFor="password">Contraseña</label>
                <input type="password" id="password" name="password" />
                <br />

                <button type="button" onClick={login}>
                    Iniciar sesión
                </button>
            </form>
        </main>
    );
}
