/**
 * Copyright 2023 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from 'react';
import { useRoutes } from 'react-router-dom';
import Index from 'src/pages';
import Chat from 'src/pages/chat';

import Onboarding from 'src/pages/onboarding';
import { useNavigate } from 'react-router-dom';

export default function Router() {
  return useRoutes([
    {
      path: 'home',
      element: (
          <Index />
      ),
    },
    {
      path: '/',
      element: (
          <Onboarding/>

      )
    },
    {
      path: '/chats',
      element: (
          <Chat />
      ),
    }
  ]);
}
