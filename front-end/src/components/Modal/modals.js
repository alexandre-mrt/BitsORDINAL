import React, { useState } from "react";
import "./modals.css";

export default function Modal() {
  const [modal, setModal] = useState(false);

  const toggleModal = () => {
    setModal(!modal);
  };
  

  if(modal) {
    document.body.classList.add('active-modal')
  } else {
    document.body.classList.remove('active-modal')
  }

  return (
    <>
      {!modal && (
        <button onClick={toggleModal} className="btn-modal">
          Mint
        </button>
      )}

      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay"></div>
          <div className="modal-content">
            <h2>Congratulations You Just Minted Your First Ordinal NFT</h2>
            <img src='https://pbs.twimg.com/media/GIO0CnuXcAEmS2x.jpg' alt="Congratulation !"/>
            <button className="close-modal" onClick={toggleModal}>
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
}
