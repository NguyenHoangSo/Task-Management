import './index.css'
import '../src/features/auth/pages/RegisterandLogin.tsx'
import RegisterandLogin from '../src/features/auth/pages/RegisterandLogin'
function App() {
  return (
    <div className='font-body-md min-h-screen flex items-center justify-center p-md'>
      <RegisterandLogin/>
    </div>

  )
}
export default App