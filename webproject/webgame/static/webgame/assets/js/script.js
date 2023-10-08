'use strict';

document.addEventListener("DOMContentLoaded", function () {
  const signupForm = document.getElementById("signup-form");

  signupForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const username = document.getElementById("username").value;
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      // ตรวจสอบข้อมูลการสมัครสมาชิก และทำการบันทึกข้อมูลลงในฐานข้อมูล (ไม่ใช่การเชื่อมต่อจริง)
      if (username && email && password) {
          alert("สมัครสมาชิกสำเร็จ!");
          // ส่งผู้ใช้ไปยังหน้าอื่น หรือส่วนที่คุณต้องการ
      } else {
          alert("กรุณากรอกข้อมูลให้ครบถ้วน");
      }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("login-form");
  const alertMessage = document.getElementById("alert-message");

  loginForm.addEventListener("submit", function (e) {
      e.preventDefault();

      // รับค่าชื่อผู้ใช้และรหัสผ่านจากฟอร์ม
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;

      // เช็คความถูกต้อง (ตัวอย่างการเช็ค)
      if (username === "Teeraphat" && password === "1234") {
          alertMessage.textContent = "your username and password are correct! you are logged in"; // ลบข้อความแจ้งเตือนเก่า (ถ้ามี)
      } else {
          // แสดง Alert และข้อความแจ้งเตือนด้านบนสุดของ login-container
          alertMessage.textContent = "your username or password is incorrect! please try again.";
      }
  });
});

/**
 * add event on multiple elements
 */

const addEventOnElements = function (elements, eventType, callback) {
  for (let i = 0, len = elements.length; i < len; i++) {
    elements[i].addEventListener(eventType, callback);
  }
}



/**
 * MOBILE NAVBAR
 * navbar will show after clicking menu button
 */

const navbar = document.querySelector("[data-navbar]");
const navToggler = document.querySelector("[data-nav-toggler]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const toggleNav = function () {
  navbar.classList.toggle("active");
  this.classList.toggle("active");
}

navToggler.addEventListener("click", toggleNav);

const navClose = () => {
  navbar.classList.remove("active");
  navToggler.classList.remove("active");
}

addEventOnElements(navLinks, "click", navClose);



/**
 * HEADER and BACK TOP BTN
 * header and back top btn will be active after scrolled down to 100px of screen
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeEl = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

window.addEventListener("scroll", activeEl);



/**
 * Button hover ripple effect
 */

const buttons = document.querySelectorAll("[data-btn]");

const buttonHoverRipple = function (event) {
  this.style.setProperty("--top", `${event.offsetY}px`);
  this.style.setProperty("--left", `${event.offsetX}px`);
}

addEventOnElements(buttons, "mousemove", buttonHoverRipple);



/**
 * Scroll reveal
 */

const revealElements = document.querySelectorAll("[data-reveal]");

const revealElementOnScroll = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    const isElementInsideWindow = revealElements[i].getBoundingClientRect().top < window.innerHeight / 1.1;

    if (isElementInsideWindow) {
      revealElements[i].classList.add("revealed");
    }
  }
}

window.addEventListener("scroll", revealElementOnScroll);

window.addEventListener("load", revealElementOnScroll);



/**
 * Custom cursor
 */

const cursor = document.querySelector("[data-cursor]");
const hoverElements = [...document.querySelectorAll("a"), ...document.querySelectorAll("button")];

const cursorMove = function (event) {
  cursor.style.top = `${event.clientY}px`;
  cursor.style.left = `${event.clientX}px`;
}

window.addEventListener("mousemove", cursorMove);

addEventOnElements(hoverElements, "mouseover", function () {
  cursor.classList.add("hovered");
});

addEventOnElements(hoverElements, "mouseout", function () {
  cursor.classList.remove("hovered");
});

