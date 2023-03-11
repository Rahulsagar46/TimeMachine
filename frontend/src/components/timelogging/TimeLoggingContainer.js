import React from 'react';
import MiddleSubSection from './MiddleSubSection';
import LeftSubcomponent from './LeftSubcomponent';
import RightSubComponent from './RightSubComponent';

const TimeLoggingContainer = ({initialinfo, setInitialinfo }) => {
    return (
        <div className='TimeLoggingMainContainer'>
            <LeftSubcomponent initialinfo={initialinfo} setInitialinfo={setInitialinfo}/>
            <MiddleSubSection initialinfo={initialinfo} setInitialinfo={setInitialinfo}/>
            <RightSubComponent initialinfo={initialinfo} />
        </div>
    );
}

export default TimeLoggingContainer