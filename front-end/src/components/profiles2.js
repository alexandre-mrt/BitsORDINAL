import React from 'react'

export default function profiles2({ Leaderboard2 }) {
  return (
        <div id="profile">
            {Item(Leaderboard2)}
        </div>
  )
}

function Item(data){
    return (
        <>
            {
                data.map((value, index) => (
                    <div className="flex" key={index}>
                        <div className="item">
                            <img src={value.img} alt=""/>
                            <div className="info">
                                <h3 className='name text-dark'>{value.name}</h3>    
                                <span>{value.dt}</span>
                            </div>                
                        </div>
                    </div>
                    )
                )
            }
        </>

    )
}