def get_app_jsx_lines(base_was_init):
    app_jsx_lines = []

    if base_was_init:
        app_jsx_lines.extend([
            "import { Route, Routes } from 'react-router-dom'\n",
            "import Nav from './components/Nav/Nav.jsx'\n",
            "import Home from './components/Home/Home.jsx'\n",
            "import Footer from './components/Footer/Footer.jsx'\n",
        ])

    app_jsx_lines.extend([
        "import './App.css'\n\n",
        "const App = () => {\n",
        "    return <>\n"
    ])

    if base_was_init:
        app_jsx_lines.extend([
            "        <Nav />\n",
            "        <main>\n",
            "           <Routes>\n",
            "               <Route path='/' element={<Home />} />\n",
            "           </Routes>\n",
            "        </main>\n",
            "        <Footer />\n"
        ])
    else:
        app_jsx_lines.append("        \n")
    
    app_jsx_lines.extend([
        "    </>\n",
        "}\n\n",
        "export default App\n"
    ])

    return app_jsx_lines
