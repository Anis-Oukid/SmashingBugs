const userProfile = document.querySelector('.user-profile');
const content = document.querySelector('.content')
const aside = document.querySelector('aside')
const fullName = $('.full-name')
const userType = $('.user-type')
const profileImage = document.querySelector('.profile-img');

const modulesText = $('.modules-text');
const settingsText = $('.settings-text');
const notificationsText = $('.notifications-text');
const logOutText = $('.logout-text');

const elsArr = [fullName, userType, modulesText, settingsText, notificationsText, logOutText];

const sideBar = $(".aside");


$(".user-profile").hover(function () {
        sideBar.stop().animate({
            width: "250px"
        }, 300);

        fullName.removeClass('hidden')
        userType.removeClass('hidden')
        modulesText.removeClass('hidden');
        settingsText.removeClass('hidden');
        notificationsText.removeClass('hidden');
        logOutText.removeClass('hidden');

        Array.from(elsArr).forEach((el) => function () {
            el.animate({
                display: "block"
            }, 300)
        });
        profileImage.classList.remove('h-7')
        profileImage.classList.remove('w-7')
        profileImage.classList.add('h-16')
        profileImage.classList.add('w-16')
    },
    function () {
        sideBar.stop().animate({
            width: "60px"
        }, 300);
        fullName.addClass('hidden')
        userType.addClass('hidden')
        modulesText.addClass('hidden');
        settingsText.addClass('hidden');
        notificationsText.addClass('hidden');
        logOutText.addClass('hidden');
        profileImage.classList.remove('h-16')
        profileImage.classList.remove('w-16')
        profileImage.classList.add('h-7')
        profileImage.classList.add('w-7')
    }
);

// sideBar.mouse
