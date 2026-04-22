import nodemailer from "nodemailer";

function createTransporter() {
  const { SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS } = process.env;

  if (SMTP_HOST && SMTP_PORT && SMTP_USER && SMTP_PASS) {
    return nodemailer.createTransport({
      host: SMTP_HOST,
      port: Number(SMTP_PORT),
      secure: Number(SMTP_PORT) === 465,
      auth: {
        user: SMTP_USER,
        pass: SMTP_PASS,
      },
    });
  }

  return nodemailer.createTransport({
    jsonTransport: true,
  });
}

const transporter = createTransporter();

async function sendEmail({ to, subject, html }) {
  const from = process.env.MAIL_FROM || process.env.SMTP_USER || "no-reply@example.com";
  const info = await transporter.sendMail({
    from,
    to,
    subject,
    html,
  });

  if (!process.env.SMTP_HOST) {
    console.log("Email preview:", info.message);
  }
}

export { transporter, sendEmail };
