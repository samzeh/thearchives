import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyDmn3OIspOCyeqEj_UrJcLeI5DktsLCqUs",
  authDomain: "archives-7aec3.firebaseapp.com",
  projectId: "archives-7aec3",
  storageBucket: "archives-7aec3.firebasestorage.app",
  messagingSenderId: "396225308779",
  appId: "1:396225308779:web:7e3c777b3c5d97472a292e",
  measurementId: "G-HNTCNTRWQ9"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app)
export const db = getFirestore(app)