import React from 'react'
import { useState } from 'react'
import TabNav from './TabNav'
import TimeLoggingContainer from '../timelogging/TimeLoggingContainer'
import VacationContainer from '../vacationmanager/VacationContainer'

const ContentContainer = ({initialinfo, setInitialinfo}) => {
    const [activeTab, setActiveTab] = useState("timeLoggingTab")
    const getComponentForActiveTab = () => {
        if (activeTab === "timeLoggingTab"){
            return (<TimeLoggingContainer initialinfo={initialinfo} setInitialinfo={setInitialinfo}/>)
        }
        if (activeTab === "vacationManagementTab"){
            return (
                <VacationContainer />
                );
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