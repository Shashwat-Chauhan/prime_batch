import React from "react";
import ReactDOM from 'react-dom/client'
import Card from './components/Card'
import Button from "./components/Button";
const domRoot = document.getElementById("parent")
const reactRoot = ReactDOM.createRoot(domRoot)


const App = () => {
    return (
        <div>
            <Button color="submit_button"> Submit </Button>
            <Card />
            <Card userName="Shashwat"></Card> 
            <Card userName="vipul"></Card> 
            <Card userName="vipin"></Card> 
            <Card userName="gogi"/>
        </div>

    )
}

reactRoot.render(<App/>)
