import React, { useEffect, useRef, useState } from "react";
import "./App.css";
import { Button, Card, Input, Radio } from "antd";
import Board from './components/board.js';
import './components/style.css';
import ParticleComponents from './components/Particles.js';
import Modal from './components/Modal/modals';
import './components/Modal/modals.css';
import Board2 from "./components/board2";




function App() {

  const [unisatInstalled, setUnisatInstalled] = useState(false);
  const [connected, setConnected] = useState(false);
  const [accounts, setAccounts] = useState<string[]>([]);
  const [publicKey, setPublicKey] = useState("");
  const [address, setAddress] = useState("");
  const [balance, setBalance] = useState({
    confirmed: 0,
    unconfirmed: 0,
    total: 0,
  });

  const [showBoard, setShowBoard] = useState(false);

  const [showModal, setModal] = useState(false);

  const [isLeaderboardOne, setIsLeaderboardOne] = useState(true);

  // Function to toggle the leaderboard
  const toggleLeaderboard = () => {
    setIsLeaderboardOne(!isLeaderboardOne);
  };

  const getBasicInfo = async () => {
    const unisat = (window as any).unisat;
    const [address] = await unisat.getAccounts();
    setAddress(address);

    const publicKey = await unisat.getPublicKey();
    setPublicKey(publicKey);

    const balance = await unisat.getBalance();
    setBalance(balance);
  };

  const selfRef = useRef<{ accounts: string[] }>({
    accounts: [],
  });
  const self = selfRef.current;
  const handleAccountsChanged = (_accounts: string[]) => {
    if (self.accounts[0] === _accounts[0]) {
      // prevent from triggering twice
      return;
    }
    self.accounts = _accounts;
    if (_accounts.length > 0) {
      setAccounts(_accounts);
      setConnected(true);

      setAddress(_accounts[0]);

      getBasicInfo();
    } else {
      setConnected(false);
    }
  };

  const handleNetworkChanged = (network: string) => {
    getBasicInfo();
  };

  useEffect(() => {

    async function checkUnisat() {
      let unisat = (window as any).unisat;

      for (let i = 1; i < 10 && !unisat; i += 1) {
          await new Promise((resolve) => setTimeout(resolve, 100*i));
          unisat = (window as any).unisat;
      }

      if(unisat){
          setUnisatInstalled(true);
      }else if (!unisat)
          return;

      unisat.getAccounts().then((accounts: string[]) => {
          handleAccountsChanged(accounts);
      });

      unisat.on("accountsChanged", handleAccountsChanged);
      unisat.on("networkChanged", handleNetworkChanged);

      return () => {
          unisat.removeListener("accountsChanged", handleAccountsChanged);
          unisat.removeListener("networkChanged", handleNetworkChanged);
      };
    }

    checkUnisat().then();
  }, []);

  if (!unisatInstalled) {
    return (
      <div className="App">
        <header className="App-header">
          <div>
            <Button
              onClick={() => {
                window.location.href = "https://unisat.io";
              }}
            >
              Install UniSat Wallet
            </Button>
          </div>
        </header>
      </div>
    );
  }
  const unisat = (window as any).unisat;


  const handleClaimClick = async () => {
    setShowBoard(true);
    setModal(true);
  };

  return (
    <div className="App" id='main'>
      <ParticleComponents id="particles" />
      <header className="App-header">
        <h1 className="wallet"> UniSat Wallet </h1>
        {connected ? (
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Card
              size="small"
              title= {<span style={{ color: 'white' }}>Description</span>}
              style={{ width: 300, margin: 10, borderRadius: 30, backgroundColor: 'rgba(65, 33, 5, 0.5)', borderBlockColor: 'rgba(65, 33, 5, 0.5)'}}
            >
              <div style={{ textAlign: "left", marginTop: 10 }}>
                <div style={{ fontWeight: "bold", color:'white' }}>Address:</div>
                <div style={{ wordWrap: "break-word", color:'white' }}>{address}</div>
              </div>

              <div style={{ textAlign: "left", marginTop: 10 }}>
                <div style={{ fontWeight: "bold", color:'white'}}>PublicKey:</div>
                <div style={{ wordWrap: "break-word", color:'white' }}>{publicKey}</div>
              </div>

              <div style={{ textAlign: "left", marginTop: 10 }}>
                <div style={{ fontWeight: "bold", color:'white' }}>Balance: (Satoshis)</div>
                <div style={{ wordWrap: "break-word", color:'white' }}>{balance.total}</div>
              </div>
            </Card>

            <Card
              className="custom-card"
              size="small"
              title={<span style={{ color: 'white' }}>Claim OGinals</span>}
              style={{ width: 300, margin: 10, borderRadius: 30,  backgroundColor: 'rgba(65, 33, 5, 0.5)', borderBlockColor: 'rgba(65, 33, 5, 0.5)' }}
            >
              <div style={{ textAlign: "left", marginTop: 10 }}>
                <div style={{ fontWeight: "bold" , color:'white'}}>Network:</div>
                <Radio.Group className="custom-radio-group"
                  onChange={async (e) => {
                    const network = await unisat.switchNetwork(e.target.value);
                  }}
                >
                  <Radio value={"livenet"}>livenet</Radio>
                  <Radio value={"testnet"}>testnet</Radio>
                </Radio.Group>
              </div>
            </Card>

            <Card
              size="small"
              title={<span style={{ color: 'white' }}>Claim OGinals</span>}
              style={{ width: 300, margin: 10, borderRadius: 30, backgroundColor: 'rgba(65, 33, 5, 0.5)', borderBlockColor: 'rgba(65, 33, 5, 0.5)' }}
            >
              <div style={{ textAlign: "left", marginTop: 10 }}>
                <div style={{ fontWeight: "bold", color: 'white'}}>OGinal Username:</div>
                <Input
                  style={{ width: 200 }}
                  onChange={(e) => {
                    console.log(e.target.value);
                  }}
                />
              </div>
              <div style={{ textAlign: "left", marginTop: 10}}>
                <Button 
                  style={{ width: 200, borderRadius: 30 }}
                onClick={handleClaimClick}> 
                Claim
                </Button>
              </div>
            </Card>
          </div>
        ) : (
          <div>
            <Button
              style={{ borderRadius: 30, backgroundColor: 'rgba(65, 33, 5, 0.5)', borderBlockColor: 'rgba(65, 33, 5, 0.5)', color: 'white' }}
              onClick={async () => {
                const result = await unisat.requestAccounts();
                handleAccountsChanged(result);
              }}
            >
              Connect UniSat Wallet
            </Button>
          </div>
        )}
      </header>
      {showBoard && <Board />  && (isLeaderboardOne ? <Board /> : <Board2 />)} 
      {showModal && <Modal onClose={toggleLeaderboard}/>}
    </div>
  );
}

export default App;
