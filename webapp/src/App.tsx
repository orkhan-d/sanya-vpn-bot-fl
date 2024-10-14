import './App.css'
import React, {useState} from "react";
import {MainButton} from "@twa-dev/sdk/react";
import WebApp from "@twa-dev/sdk";

function App() {
    const [amount, setAmount] = useState(0);

    const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setAmount(+e.target.value);
    }

    const submit = async () => {
        await fetch(
            'http://85.192.56.42:8080/',
            {
                method: 'GET',
                mode: 'no-cors'
            },
        )
    }

    return (
        <>
            <h1>Оплата подписки</h1>
            <div>
                <p>Сумма к оплате</p>
                <input type="number"
                       value={amount}
                       className={'input'}
                       onInput={onChange}/>
            </div>
            <div>
                <button className={'button'}
                        onClick={submit}>Оплатить</button>
            </div>
            <MainButton text={"Закрыть"}
                        onClick={WebApp.close}/>
        </>
    )
}

export default App
