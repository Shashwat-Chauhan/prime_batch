import { useState, useEffect } from "react";
import "./App.css";
import Card from "./Card";

function App() {
  const [data, setData] = useState([]); 

  const getData = async () => {
    try {
      const response = await fetch("https://dummyjson.com/products");
      const newData = await response.json();
      setData(newData.products);
    } catch (err) {
      console.error("Error fetching data:", err);
    } finally {
      console.log("Data fetching completed");
    }
  };

  useEffect(() => {
    getData();
  }, []); 

  return (
    <>
      {data.length > 0 ? (
        data.map((elem) => (
          <Card key={elem.id} title={elem.title} description={elem.description} />
        ))
      ) : (
        <p>Loading...</p>
      )}
    </>
  );
}

export default App;
