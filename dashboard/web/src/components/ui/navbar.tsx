import "../../styles/components/navbar.scss"
import QRCode from "../icons/qrcode";


function NavBar() {
  return (
    <nav>
      <div id="title">
        <p className="heading">Jobs Scrapper</p>
        <p className="description">Scraps the jobs over the internet</p>
      </div>
      <div id="qrcode">
        {<QRCode />}
      </div>
    </nav>
  )
}

export default NavBar;