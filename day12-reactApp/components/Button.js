const Button = ({children , color}) => {
    return(
        <button className={color}>
            {children}
        </button>      
    )
}

export default Button