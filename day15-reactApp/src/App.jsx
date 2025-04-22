import { useState } from "react";
import "./App.css";

function App() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  
  // eslint-disable-next-line no-unused-vars
  const [name, setName] = useState("");
  // eslint-disable-next-line no-unused-vars
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault()
    setName(e.target.userName.value)
    setEmail(e.target.userEmail.value)
    console.log(e);
    setIsSubmitted(true)
  };

  return (
    <div>
      {isSubmitted ? (
        <>
          <div>Cards</div>
        </>
      ) : (
        <>
          <form onSubmit={handleSubmit}>
            <section>
              <div>
                <label>Name</label>
                <input
                  placeholder="Type here..."
                  name="userName"
                />
              </div>
              <div>
                <label>Email</label>
                <input
                  placeholder="Type here..."
                  name="userEmail"
                />
              </div>
              <button onSubmit={handleSubmit} type="submit">Submit</button>
            </section>
          </form>
        </>
      )}
    </div>
  );
}

export default App;
