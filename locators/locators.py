class HomeScreenLocators:
    DIALER_BUTTON = "//android.widget.TextView[@content-desc='Phone']"

class CreateContactLocators:
    ADD_CONTACT_BUTTON = "//android.widget.ImageView[@resource-id='com.google.android.dialer:id/navigation_bar_item_icon_view'])[3]"
    CREATE_NEW_CONTACT = "//android.widget.TextView[@resource-id='com.google.android.dialer:id/empty_content_view_action'] | //android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name' and @text='Create new contact']"
    FIRST_NAME_FIELD = "//android.widget.EditText[@text='First name']"
    LAST_NAME_FIELD = "//android.widget.EditText[@text='Last name']"
    COMPANY_FIELD = "//android.widget.EditText[@text='Company']"
    PHONE_FIELD = "//android.widget.EditText[@text='Phone']"
    SAVE_BUTTON = "//android.widget.Button[@resource-id='com.google.android.contacts:id/toolbar_button']"
