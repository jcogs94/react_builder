def get_app_jsx_lines(base_was_init):
    app_jsx_lines = []

    if base_was_init:
        app_jsx_lines.extend([
            "import Nav from './components/Nav/Nav.jsx'\n",
            "import MainComponent from './components/Main/MainComponent.jsx'\n",
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
            "        <MainComponent />\n",
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
