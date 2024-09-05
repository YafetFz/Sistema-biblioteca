import React from 'react'
import ReactDOM from 'react-dom/client'

import MainIndex from './pages/main/index'
import AccesoLogin from "./pages/acceso/login"

import { createBrowserRouter, RouterProvider } from 'react-router-dom'

const router = createBrowserRouter([
	{
		path: '/',
		element: <MainIndex />,
	},
	{
		path: "/login",
		element: <AccesoLogin />
	}
])

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<RouterProvider router={router} />
	</React.StrictMode>
)