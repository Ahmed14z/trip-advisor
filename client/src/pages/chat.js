import React, { useState } from 'react';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import HomeIcon from '@mui/icons-material/Home';
import GroupIcon from '@mui/icons-material/Group';
import { useNavigate } from 'react-router-dom';

export default function Chat() {
  const [selectedTab, setSelectedTab] = useState('chats');


  const navigate = useNavigate();


   const handleTabChange = (newValue) => {

    setSelectedTab(newValue);

    switch (newValue) {
      case 'home':

        navigate('/home');
        break;
      
      case 'chats':
        navigate('/chats'); // Adjust the destination route as needed
        break;
      // Add more cases for additional tabs if needed
      default:
        break;
    }
  };



  return (
   
    <BottomNavigation
    value={selectedTab}
    onChange={(event, newValue) => handleTabChange(newValue)} // Pass only the newValue
    showLabels
    sx={{
      width: '100%',
      position: 'absolute',
      bottom: 0,
      backgroundColor: '#f1f1f1', // Adjust the background color as needed
    }}
  >
      <BottomNavigationAction label="Home" value="home" icon={<HomeIcon />} />
      <BottomNavigationAction label="Chats" value="chats" icon={<GroupIcon />} />
      {/* Add more tabs as needed */}
    </BottomNavigation>
  );
}
