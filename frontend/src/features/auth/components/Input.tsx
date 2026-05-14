type InputProps = {
    typeInp: "text" | "password" | "email",
    holder: string
}
export function Input({typeInp, holder}: InputProps) {
    return <input type={typeInp} placeholder={holder} id="" name="" required/>
}