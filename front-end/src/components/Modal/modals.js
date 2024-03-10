import React, { useState } from "react";
import "./modals.css";

export default function Modal({onClose}) {
  const [modal, setModal] = useState(false);

  const toggleModal = () => {
    setModal(!modal);
    if (!modal && onClose) { // Check if onClose is provided and modal is being closed
      onClose(); // Call the onClose function passed as prop
    }
  };
  

  if(modal) {
    document.body.classList.add('active-modal')
  } else {
    document.body.classList.remove('active-modal')
  }

  return (
    <>
      {!modal && (
        <button 
        style={{padding: "10px", borderRadius: "10px", width : 100, border: "none", cursor: "pointer", backgroundColor: "rgb(245, 166, 35)", color: "white", fontSize: "30px"}}
        onClick={toggleModal} className="btn-modal">
          Mint
        </button>
      )}

      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay"></div>
          <div className="modal-content">
          <h2 style={{ color: "rgb(245, 166, 35)" }}>Congratulations You Just Minted Your First Ordinal NFT</h2>
            <img src="/nft1.jpeg" alt="Congratulation !"/>
            <button className="close-modal" onClick={toggleModal}>
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
}
