import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import WebApp from "@twa-dev/sdk";

WebApp.ready()
WebApp.expand()

createRoot(document.getElementById('root')!).render(
    <App />
)
