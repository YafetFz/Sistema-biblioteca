import React from 'react'
import ReactDOM from 'react-dom/client'

import MainIndex from './main/index'
import AccesoLogin from "./acceso/login"

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