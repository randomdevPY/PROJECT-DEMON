import undetected_chromedriver as uc

def liveDemon(headlees=False):
    options = uc.ChromeOptions()

    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    driver = uc.Chrome(
        options=options,
        headless=headlees,
        log_level=3,
    )

    driver.maximize_window()

    return driver