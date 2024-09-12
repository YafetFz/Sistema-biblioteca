import axios from "axios"; // Librería para hacer peticiones HTTP
import React from "react";

import "../../styles/acceso/login.css";

export default function Login() {
    const [email, setEmail] = React.useState(""); // "Variables de estado" de React
    const [password, setPassword] = React.useState("");

    // React.useEffect(() => {
    //     // Ejecutar una función cuando la página cargue
    //     alert("La página ha cargado");
    // }, []);

    // React.useEffect(() => {
    //     // Ejecutar una función cuando el email cambie
    //     alert("El email ha cambiado");
    // }, [email]);

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
            <img src="/img/fondo.jpg" alt="imagen de fondo" />
            <form>
                <h1>Login</h1>
                <label htmlFor="cuenta" className="num" >Número de cuenta del carnet estudiantil</label>
                <input type="text" id="cuenta" className="cuen" name="email" placeholder="example: 7mo_012401"/>
                <button type="button" onClick={login}>
                    Ingresar 
                </button>
            </form>
        </main>
    );
}
