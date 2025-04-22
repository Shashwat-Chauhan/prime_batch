const http = require("http")
const fsPromises = require("fs/promises")
const PORT = 8080
const server = http.createServer(async(req, res) => {
    // console.log(req)
    // console.log(typeof req)
    // console.log(Object.keys(req))
    // console.log(req.url)

    res.setHeader("content-type", "text/html")
    res.setHeader("my-name", "shashwat")

    const page = await fsPromises.readFile("./index.html", {
        encoding:"utf-8"
    })

    res.end(page)   
});

server.listen(PORT, () => {
    console.log(`--------------Server Running on PORT ${PORT}------------`)
    console.log(`--------------http://localhost:${PORT}------------`)

})