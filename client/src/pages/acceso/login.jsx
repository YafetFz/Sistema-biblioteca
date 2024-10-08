import axios from "axios"; // Librería para hacer peticiones HTTP
import React from "react";

import "../../styles/acceso/login.scss";

export default function Login() {
    const email = React.useRef(null);
    const password = React.useRef(null);

    const login = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/login", {
                email: email.current.value,
                password: password.current.value,
            });

            console.log(response);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="login">
            <main>
                <img src="/img/fondo.jpg" alt="imagen de fondo" />
                <form>
                    <h1>Ingreso Administrador</h1>
                    <div>
                        <label htmlFor="email">Correo electrónico</label>
                        <br />
                        <input
                            type="email"
                            id="email"
                            name="email"
                            ref={email}
                            placeholder="example@ex.com"
                        />
                    </div>
                    <br />

                    <div>
                        <label htmlFor="password">Contraseña</label>
                        <br />
                        <input
                            type="password"
                            id="password"
                            name="password"
                            ref={password}
                            placeholder="••••••••"
                        />
                    </div>
                    <br />

                    <button type="button" onClick={login}>
                        Iniciar sesión
                    </button>
                </form>
            </main>
        </div>
    );
}
