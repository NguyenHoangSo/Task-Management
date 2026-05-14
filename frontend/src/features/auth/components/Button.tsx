type ButtonProps = {
  color: string
  backgroundColor: string
  text: string
  onClick: () => void
}

export function Button({ color, backgroundColor, text, onClick }: ButtonProps) {
  return (
    <button className={`bg-${backgroundColor}-500 hover:bg-${backgroundColor}-700 text-${color} font-bold py-2 px-4 rounded`} onClick={onClick}>
      ${text}
    </button>
  )
}