import React from 'react'
import { useState } from 'react'
import TabNav from './TabNav'
import PunchRegion from '../timelogging/PunchRegion'

const ContentContainer = ({initialinfo, setInitialinfo }) => {
    const [activeTab, setActiveTab] = useState("timeLoggingTab")
    const getComponentForActiveTab = () => {
        if (activeTab === "timeLoggingTab"){
            return (<PunchRegion login_name={initialinfo['login_name']} livestate={initialinfo['live_state']} setInfo={setInitialinfo}/>);
        }
        if (activeTab === "vacationManagementTab"){
            return (<h1>vacation</h1>);
        }
    }
    return(
        <div className='TabContainer'>
            <TabNav activeTab={activeTab} setActiveTab={setActiveTab}/>
            {getComponentForActiveTab()}
        </div>
    );
}

export default ContentContainer